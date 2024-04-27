import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { LangDropdownComponent } from './lang-dropdown/lang-dropdown.component';
import { ProfileDropdownComponent } from './profile-dropdown/profile-dropdown.component';
import { MobileMenuComponent } from './mobile-menu/mobile-menu.component';
import { HeaderNavigationComponent } from './header-navigation/header-navigation.component';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    LangDropdownComponent,
    ProfileDropdownComponent,
    MobileMenuComponent,
    HeaderNavigationComponent,
  ],
  templateUrl: './header.component.html',
})
export class HeaderComponent {}
