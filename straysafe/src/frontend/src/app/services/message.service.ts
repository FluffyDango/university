import { inject, Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  private client = inject(HttpClient);

  getHello(): Observable<string> {
    return this.client.get<string>('http://localhost:8080/hello', { responseType: 'text' as 'json' });
  }
}
