import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SharedService {
  sharedVariable: any;

  constructor() {}

  setSharedVariable(value: any) {
    this.sharedVariable = value;
  }

  getSharedVariable() {
    return this.sharedVariable;
  }
}
    