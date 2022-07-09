import { BellIcon, SearchIcon } from '@heroicons/react/solid'
import Link from 'next/link'
import { useEffect, useState } from 'react'
import useAuth from '../hooks/useAuth'

function Header() {
    const [isScrolled, setIsScrolled] = useState(false)
    const { logout } = useAuth()

    useEffect(() => {
      const handleScroll = () => {
        if (window.scrollY > 0) {
          setIsScrolled(true)
        } else {
          setIsScrolled(false)
        }
      }
  
      window.addEventListener('scroll', handleScroll)
  
      return () => {
        window.removeEventListener('scroll', handleScroll)
      }
    }, [])

    return (
      <header className={`${isScrolled && 'bg-[#ffffff]'}`}>
      <div className="flex items-center space-x-2 md:space-x-10">
      <img
        src="/nbdt-gsoc-pic-removebg.png"
        width={100}
        height={100}
        className="absolute left-4 top-4 cursor-pointer object-contain md:left-10 md:top-6"
      />
      </div>

      <ul className="hidden space-x-4 md:flex">
        <li className="headerLink">Home</li>
        <li className="headerLink">Recommendations</li>
        <li className="headerLink">Add Reviewers</li>
        <li className="headerLink">Bookmark Reviewers</li>
      </ul>

      <div className="flex items-center space-x-4 text-sm font-light">
            <SearchIcon className="hidden h-6 w-6 sm:inline"/>
            <p className="hidden lg:inline">Reviewers</p>
            <BellIcon className="h-6 w-6"/>
            {/*<Link href="/account">*/}
                <img
                    onClick={logout}
                    src="/account.png"
                    alt=""
                    width={25}
                    height={25}
                    className="cursor-pointer rounded"
                />
            {/*</Link>*/}
            <Link href="/login">
                <img
                    
                    src="/Login.png"
                    alt=""
                    width={100} 
                    className="cursor-pointer rounded"
                />
            </Link>
            <Link href="/register">
                <img
                    src="/Register.png"
                    alt=""
                    width={100}
                    className="cursor-pointer rounded"
                />
            </Link>
        </div>

  </header>
    )
  }
  
  export default Header