import { useSession} from 'next-auth/react'
import redirect from 'nextjs-redirect'
import Link from 'next/link'
import { useState, useEffect } from 'react';


export default function Header() {  

    const [token, setToken] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('token');
        setToken(token)
    }, []);

    const handleSignin = (e) => {
        e.preventDefault()
        if(!token)
        {
            redirect('/signin')
        }
    }

    const handleSignout = (e) => {
        e.preventDefault()
        if(token)
        {
            localStorage.removeItem('token')
            redirect('/login')
        }
    }

    const { data: session } = useSession();

    return (
      <div className='header'>
        <Link href='/'>
          <a className='logo'>AppLogo</a>
        </Link>
             {token && <a href="#" onClick={handleSignout} className="btn-signin">SIGN OUT</a>  } 
             {!token && <a href="#" onClick={handleSignin}  className="btn-signin">SIGN IN</a>  } 
      </div>

    )
  }