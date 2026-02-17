import { NextResponse } from 'next/server';

const TOKEN_COOKIE_NAME = 'auth_token';

export async function POST() {
  const response = NextResponse.json({ success: true, message: 'Logged out successfully' });
  response.cookies.delete(TOKEN_COOKIE_NAME);
  return response;
}
