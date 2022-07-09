import '../styles/globals.css'
import type { AppProps } from 'next/app'
import { AuthProvider } from '../hooks/useAuth'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    // HOC --> Higher order component
  <AuthProvider>
    <Component {...pageProps} />
  </AuthProvider>
  )
}

export default MyApp
