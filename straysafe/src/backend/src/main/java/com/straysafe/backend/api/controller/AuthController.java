//package com.straysafe.backend.api.controller;
//
//import com.straysafe.backend.api.model.request.UserCredentialRequest;
//import com.straysafe.backend.api.model.response.UserCredentialResponse;
//import com.straysafe.backend.service.UserAuthService;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.http.ResponseEntity;
//import org.springframework.web.bind.annotation.PostMapping;
//import org.springframework.web.bind.annotation.RequestBody;
//import org.springframework.web.bind.annotation.RestController;
//
//@RestController
//public class AuthController {
//
//    private final UserAuthService userAuthService;
//
//    @Autowired
//    public AuthController(UserAuthService userAuthService) {
//        this.userAuthService = userAuthService;
//    }
//
//    @PostMapping("/login")
//    public ResponseEntity<UserCredentialResponse> login(@RequestBody UserCredentialRequest userCredentials) {
//        UserCredentialResponse user = userAuthService.login(userCredentials);
//        return ResponseEntity.ok(user);
//    }
//}
