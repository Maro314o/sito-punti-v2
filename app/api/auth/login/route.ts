import { NextRequest, NextResponse } from 'next/server';

const API_URL = process.env.NEXT_PUBLIC_FLASK_API_URL || 'http://localhost:5328';
const TOKEN_COOKIE_NAME = 'auth_token';

export async function POST(request: NextRequest) {
  const body = await request.json();
  
  const response = await fetch(`${API_URL}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  const data = await response.json();

  if (data.success && data.token) {
    const nextResponse = NextResponse.json(data, { status: response.status });
    
    nextResponse.cookies.set(TOKEN_COOKIE_NAME, data.token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: 60 * 60 * 24 * 7,
      path: '/',
    });
    
    return nextResponse;
  }

  return NextResponse.json(data, { status: response.status });
}
