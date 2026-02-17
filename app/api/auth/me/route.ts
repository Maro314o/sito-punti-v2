import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const API_URL = process.env.NEXT_PUBLIC_FLASK_API_URL || 'http://localhost:5328';

export async function GET(request: NextRequest) {
  let token = request.headers.get('x-auth-token');
  
  if (!token) {
    const cookieStore = request.cookies.get('auth_token');
    token = cookieStore?.value || null;
  }
  
  if (!token) {
    return NextResponse.json({ error: 'Not authenticated' }, { status: 401 });
  }

  const response = await fetch(`${API_URL}/api/auth/me`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await response.json();
  return NextResponse.json(data, { status: response.status });
}
