import { Component } from '@angular/core';
import { clickedOutside } from '../../../directives/clickedOutside.directive';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-mobile-menu',
  standalone: true,
  imports: [CommonModule, clickedOutside, RouterLink],
  templateUrl: './mobile-menu.component.html'
})
export class MobileMenuComponent {
  dropdownOpen: boolean = false;

  toggleDropdown(): void {
    this.dropdownOpen = !this.dropdownOpen;
  }

  onClickedOutside(): void {
    this.dropdownOpen = false;
  }
}
