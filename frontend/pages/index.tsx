import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Header from '../components/Header'

const Home: NextPage = () => {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center py-2">
      <Head>
        <title>Home - NBDT-GSoC</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header/>
      <main>

      </main>

      

      <footer className="flex  justify-center border-t">
        <a
          className="flex items-center justify-center gap-2"
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          NBDT{' '}
          <Image src="/nbdt-gsoc-pic.png" alt="NBDT-GSoC Logo" width={81} height={45} />
        </a>
      </footer>
    </div>
  )
}

export default Home
