import Head from 'next/head'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { SubmitHandler } from 'react-hook-form'
import useAuth from '../hooks/useAuth'


interface Inputs{
    email: string
    password: string
}

function Login() {
    const [login, setLogin] = useState(false)
    const { signIn, signUp } = useAuth()

    const { register, 
            handleSubmit, 
            formState: { errors }, } = useForm<Inputs>();
    const onSubmit:  SubmitHandler<Inputs> = async data => {
        console.log(data)
        if (login) {
            await signIn(data.email, data.password)
        } else {
            await signUp(data.email, data.password)
        }

    }

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

      <form 
        onSubmit={handleSubmit(onSubmit)}
        className="relative mt-24 space-y-8 rounded bg-black/80 py-10 px-6 md:mt-0 md:max-w-md md:px-14">
        <h1 className="text-4xl text-white font-semibold">Sign In</h1>
        <div className="space-y-4">
            <label className="inline-block w-full">
                <input type="email" placeholder="Email" className="input"  {...register('email', { required: true })}/>
                {errors.email && (
                    <p className="p-1 text-[13px] font-light  text-orange-500">
                    Please enter a valid email.
                    </p>
                )}
            </label>
    
            <label className="inline-block w-full">
                <input type="password" placeholder="Password" className="input" {...register('password', { required: true })}/>
                {errors.password && (
                    <p className="p-1 text-[13px] font-light  text-orange-500">
                        Your password must contain between 4 and 60 characters.
                    </p>
                 )}
            </label>
        </div>

        <button 
            className="w-full rounded bg-[#18A0FB] py-3 font-semibold"
            onClick={() => setLogin(true)}>Sign In</button>
        
        <div className="text-[gray]">   
            Not registered?{' '}
            <button type="submit" 
                className="text-white hover:underline"
                onClick={() => setLogin(false)}>Sign Up now</button>
        </div>
      </form>
    </div>
  )
}

export default Login