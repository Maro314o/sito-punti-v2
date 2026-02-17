const API_URL = '';

export interface User {
  id: number;
  email: string;
  nominativo: string;
  admin: boolean;
  account_attivo: boolean;
  squadra?: string;
  classe_id?: number;
}

export async function fetchAPI(endpoint: string, options: RequestInit = {}) {
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ error: 'Request failed' }));
    throw new Error(error.error || 'Request failed');
  }

  return response.json();
}

export async function login(email: string, password: string) {
  return fetchAPI('/api/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });
}

export async function logout() {
  return fetchAPI('/api/auth/logout', {
    method: 'POST',
  });
}

export async function getCurrentUser(): Promise<User | null> {
  try {
    return await fetchAPI('/api/auth/me');
  } catch {
    return null;
  }
}

export async function checkAuth(): Promise<{ authenticated: boolean; user?: User }> {
  try {
    return await fetchAPI('/api/auth/check');
  } catch {
    return { authenticated: false };
  }
}

export async function getClasses() {
  return fetchAPI('/api/proxy/classes');
}

export async function getClass(classId: number) {
  return fetchAPI(`/api/proxy/classes/${classId}`);
}

export async function getSquadreByClass(classId: number) {
  return fetchAPI(`/api/proxy/classes/${classId}/squadre`);
}

export async function getStudents() {
  return fetchAPI('/api/proxy/students');
}

export async function getStudent(studentId: number) {
  return fetchAPI(`/api/proxy/students/${studentId}`);
}

export async function getStudentPoints(studentId: number, stagione: number) {
  return fetchAPI(`/api/proxy/students/${studentId}/points?stagione=${stagione}`);
}

export async function getSquadraPoints(squadraId: number, stagione: number) {
  return fetchAPI(`/api/proxy/squadre/${squadraId}/points?stagione=${stagione}`);
}
