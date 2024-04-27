import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import * as L from 'leaflet';
import { SharedService } from '../../../services/shared.service';

@Component({
  selector: 'app-address-input',
  standalone: true,
  imports: [RouterLink, FormsModule, LeafletModule],
  templateUrl: './address-input.component.html',
})
export class AddressInputComponent {
  private map: L.Map | null = null;
  private marker: L.Marker | null = null;
  address: string = ''; // Taken from the input field in the template

  constructor(private sharedService: SharedService) {}

  updateSharedVariable() {
    this.sharedService.setSharedVariable(this.address);
  }

  options = {
    layers: [
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        minZoom: 3,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }),
    ],
    zoom: 8,
    center: L.latLng(55.27914, 24.02161),
  };

  onMapReady(map: L.Map): void {
    this.map = map;
  }

  searchAddress(): void {
    if (!this.address.trim()) return;
    const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(this.address)}`;
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        if (data && Array.isArray(data)) {
          const { lat, lon } = data[0];
          if (this.map) {
            this.map.flyTo([lat, lon], 16);
            if (this.marker) {
              this.map.removeLayer(this.marker);
            }
            this.marker = L.marker([lat, lon]).addTo(this.map);
          }
        } else {
          alert('Address not found');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        alert('Failed to search the address');
      });
  }
}
