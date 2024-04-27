export interface UserCredentialRequest {
  login: string;
  password: string;
}

export interface UserCredentialResponse {
  id: number;
  firstName: string;
  lastName: string;
  login: string;
  token: string;
}
