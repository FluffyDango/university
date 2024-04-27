import { inject, Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { UserCredentialRequest,UserCredentialResponse } from "../types";

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private client = inject(HttpClient);

  login(inputs: Partial<UserCredentialRequest>): Observable<UserCredentialResponse> {
    return this.client.post<UserCredentialResponse>('http://localhost:8080/login',inputs);
  }
}
