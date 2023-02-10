import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Navbar from './Navbar';

export default function Author() {
  const [user, setUser] = useState(null);
  const router = useRouter();

  const {
    query: { abstract },
  } = router;

  const props = {
    abstract: abstract
  }

  const authors = [
    {
      name: "John Doe",
      email: "john.doe@gmail.com"
    },
    {
      name: "Jane Doe",
      email: "jane.doe@gmail.com"
    },
    {
      name: "John Smith",
      email: "john.smith@gmail.com"
    },
    {
      name: "Jane Smith",
      email: "jane.smith@gmail.com"
    },
    {
      name: "John Johnson",
      email: "john.johnson@gmail.com"
    },
    {
      name: "Jane Johnson",
      email: "jane.johnson@gmail.com"
    },
  ]

  useEffect(() => {
    const token = localStorage.getItem('token');
    async function fetchUser() {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/users/me/`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (res.status == 200) {
        const json = await res.json();
        setUser(json);
      } else {
        router.push('login');
      }
    }
    fetchUser();
  }, []);

  return (
    <div>
      <Navbar />

      <div>
        <h1 className="text-3xl font-bold" style={
          {
            marginLeft: "2%",
            marginTop: "3%",
            marginBottom: "2%",
          }
        }>
          Author Page
        </h1>

        <div className="text-xl" style={
          {
            marginLeft: "2%",
            marginTop: "3%",
            marginBottom: "2%",
          }
        }>
          <p>
            Based on your abstract/title that you have submitted, <br /> 
            <i>{props.abstract}</i> <br />
            Here are some authors that you
            might be interested in:
          </p>
          <div>
          {authors.map((author) => {
            return (
              <div>
                <p>{author.name}</p>
                <p>{author.email}</p>
              </div>
            )
          })}
            
          </div>
        </div>

        {/* {user && (
          <p>{user.username}</p>
        )} */}

      </div>
    </div>
  )
}