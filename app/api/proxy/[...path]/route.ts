import { NextRequest, NextResponse } from 'next/server';
import { cookies } from 'next/headers';

const API_URL = process.env.NEXT_PUBLIC_FLASK_API_URL || 'http://localhost:5328';
const TOKEN_COOKIE_NAME = 'auth_token';

export async function GET(request: NextRequest) {
  const cookieStore = await cookies();
  const token = cookieStore.get(TOKEN_COOKIE_NAME)?.value;
  
  const path = request.nextUrl.pathname.replace('/api/proxy', '');
  const url = new URL(path, API_URL);
  url.search = request.nextUrl.search.toString();

  const headers: HeadersInit = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const response = await fetch(url.toString(), { method: 'GET', headers });
  return NextResponse.json(await response.json(), { status: response.status });
}

export async function POST(request: NextRequest) {
  const cookieStore = await cookies();
  const token = cookieStore.get(TOKEN_COOKIE_NAME)?.value;
  
  const path = request.nextUrl.pathname.replace('/api/proxy', '');
  const url = new URL(path, API_URL);
  
  const headers: HeadersInit = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const response = await fetch(url.toString(), { method: 'POST', headers, body: await request.text() });
  return NextResponse.json(await response.json(), { status: response.status });
}

export async function PUT(request: NextRequest) {
  const cookieStore = await cookies();
  const token = cookieStore.get(TOKEN_COOKIE_NAME)?.value;
  
  const path = request.nextUrl.pathname.replace('/api/proxy', '');
  const url = new URL(path, API_URL);
  
  const headers: HeadersInit = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const response = await fetch(url.toString(), { method: 'PUT', headers, body: await request.text() });
  return NextResponse.json(await response.json(), { status: response.status });
}

export async function DELETE(request: NextRequest) {
  const cookieStore = await cookies();
  const token = cookieStore.get(TOKEN_COOKIE_NAME)?.value;
  
  const path = request.nextUrl.pathname.replace('/api/proxy', '');
  const url = new URL(path, API_URL);
  
  const headers: HeadersInit = {};
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const response = await fetch(url.toString(), { method: 'DELETE', headers });
  return NextResponse.json(await response.json(), { status: response.status });
}
