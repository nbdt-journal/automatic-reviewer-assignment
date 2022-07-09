import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Header from '../components/Header'
import Row from '../components/Row'
const Home: NextPage = () => {
  return (
    <div className="relative h-screen bg-gradient-to-b from-pink-900/10 to-[#a7dcf5] lg:h-[140vh]">
      <Head>
        <title>automatic-reviewer-assignment</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header/>
      <main>
        <section>
        <Row/> 
        </section>

      </main>
      
        

      <footer className="flex h-24 w-full items-center justify-center border-t">
        <a
          className="flex items-center justify-center gap-2"
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          NBDT x GSoC {' '}
          <Image src="/nbdt-gsoc-pic-removebg.png" alt="Vercel Logo" width={81} height={45} />
        </a>
      </footer>
    </div>
  )
}


export default Home
