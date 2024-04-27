import { Component, EventEmitter, inject, Output } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { LoginService } from "../../services/login.service";
import { UserCredentialRequest } from "../../types";

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent{
  @Output() onSubmitLoginEvent = new EventEmitter();
  service = inject(LoginService);
  login : string = "";
  password : string = "";

  onSubmitLogin(): void {
    this.service.login((this.login, this.password) as Partial<UserCredentialRequest>)
  }


}
