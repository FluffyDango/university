import { Routes } from '@angular/router';
import { HomeComponent } from './components/home-page/home-page.component';
import { TipsComponent } from './components/tips-page/tips-page.component';
import { GridViewComponent } from './components/grid-view/grid-view.component';
import { Page404Component } from './components/page-404/page-404.component';
import { LostPetPageComponent } from './components/report-components/lost-pet-page/lost-pet-page.component';
import { FoundPetPageComponent } from './components/report-components/found-pet-page/found-pet-page.component';
import { SearchImageComponent } from './components/search/search-image/search-image.component';
import { SearchMapComponent } from './components/search/search-map/search-map.component';
import { LoginComponent } from "./components/login/login.component";

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'login', component: LoginComponent},
    { path: 'tips', component: TipsComponent },
    { path: 'lost-pet', component: LostPetPageComponent },
    { path: 'found-pet', component: FoundPetPageComponent },
    { path: 'search/image', component: SearchImageComponent },
    { path: 'search/reports', component: GridViewComponent },
    { path: 'search/map', component: SearchMapComponent },
    { path: 'page-404', component: Page404Component },
    { path: '**', redirectTo: '/page-404' }
];
