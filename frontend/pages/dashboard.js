import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Navbar from './Navbar';

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [abstract, setAbstract] = useState("");
  const router = useRouter();

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
            marginLeft: "5%",
            marginTop: "3%",
            marginBottom: "2%",
          }
        }>
          Welcome to the NBDT Dashboard
        </h1>
      </div>
      <textarea
        className="border-2 border-gray-300 bg-white h-96 rounded-lg px-4 py-2 resize-none focus:outline-none focus:border-black"
        style={
          {
            width: "90%",
            marginLeft: "5%",
            marginBottom: "2%",
          }
        }
        placeholder="Enter your abstract here"
        value={abstract}
        onChange={(e) => setAbstract(e.target.value)}
      />
      {/* Put button on the right side */}

      <div style={
        {
          marginRight: "5%",
          textAlign: "right",
        }
      }>
        <button
          // className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded text-right"
          style={
            {
              marginBottom: "2%",
              backgroundColor: "#5E6CB4",
              border: "none",
              color: "white",
              padding: "5px 16px",
              textAlign: "center",
              fontSize: "16px",
              margin: "4px 2px"
            }
          }
          onClick={() => {
            // Redirect to author page
            router.push({
              pathname: '/author',
              query: { abstract },
            });

            alert({ abstract });
          }}
        >
          Find Authors
        </button>
        <button
          // className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded text-right"
          style={
            {
              marginBottom: "2%",
              backgroundColor: "#5E6CB4",
              border: "none",
              color: "white",
              padding: "5px 16px",
              textAlign: "center",
              fontSize: "16px",
              margin: "4px 2px"
            }
          }
          onClick={() => {
            // Redirect to author page
            router.push({
              pathname: '/author',
              query: { abstract },
            });

            alert({ abstract });
          }}
        >
          Find Articles
        </button>
        <button
          // className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded text-right"
          style={
            {
              marginBottom: "2%",
              backgroundColor: "#5E6CB4",
              border: "none",
              color: "white",
              padding: "5px 16px",
              textAlign: "center",
              fontSize: "16px",
              margin: "4px 2px"
            }
          }
          onClick={() => {
            // Redirect to author page
            router.push({
              pathname: '/author',
              query: { abstract },
            });

            alert({ abstract });
          }}
        >
          Find Journals
        </button>
      </div>
      {/* {user && (
        <p>{user.username}</p>
      )} */}
    </div>
  )
}