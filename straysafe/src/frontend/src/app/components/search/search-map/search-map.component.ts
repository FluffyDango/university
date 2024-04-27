import { Component } from '@angular/core';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';
import { LeafletMarkerClusterModule } from '@asymmetrik/ngx-leaflet-markercluster';
import * as L from 'leaflet';
import 'leaflet.markercluster';

@Component({
  selector: 'app-search-map',
  standalone: true,
  imports: [LeafletModule, LeafletMarkerClusterModule],
  templateUrl: './search-map.component.html'
})
export class SearchMapComponent {
  private map!: L.Map;
  private markerClusterGroup!: L.MarkerClusterGroup;
  address: string = ''; // Taken from the input field in the template

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
    this.markerClusterGroup = new L.MarkerClusterGroup();
    this.map.addLayer(this.markerClusterGroup);

    const markers = [
      { lat: 55.27914, lng: 24.02161, title: 'Marker 1' },
      { lat: 55.28414, lng: 24.02561, title: 'Marker 2' }
    ];

    markers.forEach(marker => {
      const leafletMarker = L.marker([marker.lat, marker.lng], {
        title: marker.title,
        icon: L.icon({
          iconUrl: 'marker-icon.png',
          iconSize: [25, 41],
          iconAnchor: [12, 41],
        })
      });

      this.markerClusterGroup.addLayer(leafletMarker);
    });
  }
}
