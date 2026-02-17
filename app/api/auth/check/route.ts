import { NextRequest, NextResponse } from 'next/server';
import { cookies } from 'next/headers';

const API_URL = process.env.NEXT_PUBLIC_FLASK_API_URL || 'http://localhost:5328';
const TOKEN_COOKIE_NAME = 'auth_token';

export async function GET() {
  const cookieStore = await cookies();
  const token = cookieStore.get(TOKEN_COOKIE_NAME)?.value;
  
  if (!token) {
    return NextResponse.json({ authenticated: false });
  }

  const response = await fetch(`${API_URL}/api/auth/check`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await response.json();
  return NextResponse.json(data);
}
