import { CommonModule } from '@angular/common';
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-image-upload',
  standalone: true,
  imports: [RouterLink, CommonModule],
  templateUrl: './image-upload.component.html',
})
export class ImageUploadComponent {
  @ViewChild('imageCanvas') canvasRef!: ElementRef<HTMLCanvasElement>;
  file: File | null = null;
  private canvas!: HTMLCanvasElement;
  private ctx: CanvasRenderingContext2D | null = null;
  private circle = { x: 0, y: 0, radius: 64 };
  private isDragging = false;
  private isResizing = false;
  private loadedImage: HTMLImageElement | null = null;

  handleFileInput(event: any) {
    const files = event.target.files;
    if (files.length > 0) {
      this.file = files[0];
      const reader = new FileReader();
      reader.onload = (loadEvent: any) => {
        this.initializeCanvas();
        this.loadAndDrawImage(loadEvent.target.result);
      };
      reader.readAsDataURL(files[0]);
    }
  }

  onDragOver(event: DragEvent) {
    event.preventDefault(); // Necessary to allow the drop
    event.stopPropagation();
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    event.stopPropagation();
    const files = event.dataTransfer?.files;
    if (files && files.length > 0) {
      this.handleFileInput({target: {files: files}});
    }
  }

  calculateMousePosition(event: MouseEvent): {
    mouseX: number;
    mouseY: number;
  } {
    const rect = this.canvas.getBoundingClientRect();
    const scaleX = this.canvas.width / rect.width;
    const scaleY = this.canvas.height / rect.height;
    const mouseX = (event.clientX - rect.left) * scaleX;
    const mouseY = (event.clientY - rect.top) * scaleY;
    return { mouseX, mouseY };
  }

  initializeCanvas() {
    if (!this.canvasRef) return;
    this.canvas = this.canvasRef.nativeElement;
    this.ctx = this.canvas.getContext('2d');
    this.canvas.width = this.canvas.offsetWidth;
    this.canvas.height = this.canvas.offsetHeight;

    this.circle.x = this.canvas.width / 2;
    this.circle.y = this.canvas.height / 2;

    // Event listeners for dragging
    this.canvas.addEventListener('mousedown', this.startDragging.bind(this));
    // Add a throttle to prevent the event from firing too often (Optimization)
    this.canvas.addEventListener('mousemove', this.throttle(this.dragCircle.bind(this), 10));
    this.canvas.addEventListener('mouseup', this.stopDragging.bind(this));
    this.canvas.addEventListener('mouseleave', this.stopDragging.bind(this));
  }

  loadAndDrawImage(imageUrl: string) {
    const image = new Image();
    image.onload = () => {
      this.loadedImage = image;
      this.draw(image);
    };
    image.src = imageUrl;
  }

  draw(image: HTMLImageElement) {
    if (!this.ctx) return;
    const fixedCanvasWidth = this.canvas.width;
    const scale = fixedCanvasWidth / image.width;
    const scaledImageHeight = image.height * scale;
    this.canvas.height = scaledImageHeight;

    // Black background with 50% opacity
    this.ctx.clearRect(0, 0, fixedCanvasWidth, scaledImageHeight);
    this.ctx.drawImage(image, 0, 0, fixedCanvasWidth, scaledImageHeight);
    this.ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    this.ctx.fillRect(0, 0, fixedCanvasWidth, scaledImageHeight);

    // Circle of pet in the photo
    this.ctx.globalCompositeOperation = 'destination-out';
    this.ctx.beginPath();
    this.ctx.arc(this.circle.x, this.circle.y, this.circle.radius, 0, Math.PI * 2);
    this.ctx.fill();
    this.ctx.globalCompositeOperation = 'source-over';
  }

  dragCircle(event: MouseEvent) {
    if (!this.loadedImage || (!this.isDragging && !this.isResizing)) return;
    const { mouseX, mouseY } = this.calculateMousePosition(event);

    if (this.isDragging) {
      this.circle.x = mouseX;
      this.circle.y = mouseY;
    } else if (this.isResizing) {
      // Pythagorean theorem to calculate the distance between the center of the circle and the mouse
      const newRadius = Math.sqrt(Math.pow(mouseX - this.circle.x, 2) + Math.pow(mouseY - this.circle.y, 2));
      this.circle.radius = newRadius;
    }

    this.draw(this.loadedImage);
  }

  startDragging(event: MouseEvent) {
    if (!this.canvas || !this.loadedImage) return;
    const { mouseX, mouseY } = this.calculateMousePosition(event);
    const distanceFromCenter = Math.sqrt(Math.pow(mouseX - this.circle.x, 2) + Math.pow(mouseY - this.circle.y, 2));

    if (distanceFromCenter < this.circle.radius + 50 && distanceFromCenter > this.circle.radius - 50) {
      this.isResizing = true;
    } else if (distanceFromCenter < this.circle.radius) {
      this.isDragging = true;
    }
  }

  stopDragging() {
    this.isDragging = false;
    this.isResizing = false;
  }

  // Throttle function to prevent the event from firing too often
  throttle(callback: (this: any, ...args: any[]) => void, limit: number): (...args: any[]) => void {
    let waiting = false; // Initially, we're not waiting
    return function (this: any, ...args: any[]): void {
      // We return a throttled function
      if (!waiting) {
        // If we're not waiting
        callback.apply(this, args); // Execute users function
        waiting = true; // Prevent future invocations
        setTimeout(function (this: any) {
          // After a period of time
          waiting = false; // And allow future invocations
        }, limit);
      }
    };
  }
}
