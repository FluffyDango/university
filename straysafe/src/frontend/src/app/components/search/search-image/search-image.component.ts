import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from '../../../services/api-service.service';

@Component({
  selector: 'app-search-image',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './search-image.component.html'
})
export class SearchImageComponent {
  posts: any;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.pythonTestHelloWorld().subscribe((data: any) => {
      this.posts = data;
      console.log(this.posts)
    });
  }
}
