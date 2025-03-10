import Head from 'next/head'

function Register() {
  return (
      <div className="flex min-h-screen flex-col items-center justify-center py-2">
        <Head>
            <title>automatic-reviewer-assignment</title>
            <link rel="icon" href="/favicon.ico" />
        </Head>

      

        <img
        src="/nbdt-gsoc-pic-removebg.png"
        width={100}
        height={100}
        className="absolute left-4 top-4 cursor-pointer object-contain md:left-10 md:top-6"
      />

      <form className="relative mt-24 space-y-8 rounded bg-black/80 py-10 px-6 md:mt-0 md:max-w-md md:px-14">
        <h1 className="text-4xl text-white font-semibold">Sign Up</h1>
        <div className="space-y-4">
            <label className="inline-block w-full">
                <input type="first name" placeholder="First Name" className="input" />
            </label>
            <label className="inline-block w-full">
                <input type="last name" placeholder="Last Name" className="input" />
            </label>
            <label className="inline-block w-full">
                <input type="affiliation" placeholder="Affiliation" className="input" />
            </label>
            <label className="inline-block w-full">
                <input type="email" placeholder="Email" className="input" />
            </label>
            <label className="inline-block w-full">
            <input type="password" placeholder="Password" className="input"/>
            </label>
        </div>

        <button className="w-full rounded bg-[#18A0FB] py-3 font-semibold text-white">Register</button>
        

      </form>
    </div>
  )
}

export default Register