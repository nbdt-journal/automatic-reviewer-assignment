import { NextResponse, NextRequest } from 'next/server'
export async function middleware(req, ev) {
    const { pathname } = req.nextUrl
    if (pathname == '/signin') {
        return NextResponse.redirect('/signin')
    }
    return NextResponse.next()
}