function Header() {
  return (
    <header>
        <div className="flex items-center space-x-2 md:space-x-10">
            <img src="/nbdt-gsoc-pic.png" 
            alt="NBDT-GSoC logo" 
            width={100}
            height={100}
            className="cursor-pointer object-contain"/>

            <ul className="hidden space-x-4 md:flex">
                <li className="headerLink">Home</li>
                <li className="headerLink">Recommendations</li>
                <li className="headerLink">Add Reviewers</li>
            </ul>
        </div>

    </header>
    
  )
}

export default Header