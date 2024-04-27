import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'home',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './home-page.component.html'
})
export class HomeComponent {

}
