import {
  Directive,
  ElementRef,
  Output,
  EventEmitter,
  HostListener,
} from '@angular/core';

@Directive({
  selector: '[clickedOutside]',
  standalone: true,
})
export class clickedOutside {
  // Near the directive there should be a (clickOutside) event which gets triggered when the user clicks outside the directive
  @Output() clickOutside = new EventEmitter<void>();

  // Get the parent element of the directive
  constructor(private element: ElementRef) {}

  // Listen for click events and check if the clicked element is outside the directive
  @HostListener('document:click', ['$event.target'])
  public onDocumentClick(target: any): void {
    const clickedInside = this.element.nativeElement.contains(target);
    if (!clickedInside) {
      this.clickOutside.emit();
    }
  }
}
