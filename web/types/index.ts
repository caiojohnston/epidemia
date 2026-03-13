// User types
export interface User {
  id: string
  email: string
  name: string
  role: "admin" | "user"
  createdAt: string
  updatedAt: string
}

// Auth types
export interface LoginCredentials {
  email: string
  password: string
}

export interface AuthResponse {
  access_token: string
  token_type: string
  user: User
}

// API Response types
export interface ApiResponse<T> {
  data: T
  message?: string
}

export interface ApiError {
  detail: string
  status_code: number
}

// Pagination
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
  pages: number
}
