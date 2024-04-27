import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private springApiUrl = environment.springApiUrl;
  private pythonApiUrl = environment.pythonApiUrl;

  constructor(private http: HttpClient) { }

  pythonTestHelloWorld(): Observable<any[]> {
    return this.http.get<any[]>(`${this.pythonApiUrl}/api/hello`);
  }

  getReports(): Observable<any[]> {
    return this.http.get<any[]>(`${this.springApiUrl}/reports`);
  }

  postReport(report: any): Observable<any> {
    return this.http.post<any>(`${this.springApiUrl}/reports/create`, report);
  }

  // getPostById(id: number): Observable<any> {
  //   return this.http.get<any>(`${this.springApiUrl}/posts/${id}`);
  // }

  // addPost(post: any): Observable<any> {
  //   return this.http.post<any>(`${this.springApiUrl}/posts`, post);
  // }

  // updatePost(id: number, post: any): Observable<any> {
  //   return this.http.put<any>(`${this.springApiUrl}/posts/${id}`, post);
  // }

  // deletePost(id: number): Observable<any> {
  //   return this.http.delete<any>(`${this.springApiUrl}/posts/${id}`);
  // }
}