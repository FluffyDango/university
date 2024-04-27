//package com.straysafe.backend.service;
//
//import com.straysafe.backend.api.model.exception.AppException;
//import com.straysafe.backend.api.model.request.UserCredentialRequest;
//import com.straysafe.backend.api.model.response.UserCredentialResponse;
//import com.straysafe.backend.domain.UserCredentialDAOResponse;
//import com.straysafe.backend.repository.UserAuthRepository;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.context.ApplicationContextException;
//import org.springframework.http.HttpStatus;
//import org.springframework.security.crypto.password.PasswordEncoder;
//import org.springframework.stereotype.Service;
//
//import java.nio.CharBuffer;
//
//@Service
//public class UserAuthService {
//
////    UserAuthRepository userAuthRepository;
////    PasswordEncoder passwordEncoder;
////
////    @Autowired
////    public UserAuthService(UserAuthRepository userAuthRepository, PasswordEncoder passwordEncoder) {
////        this.userAuthRepository = userAuthRepository;
////        this.passwordEncoder = passwordEncoder;
////    }
////
////    public UserCredentialResponse login(UserCredentialRequest userCredentials) {
////        UserCredentialDAOResponse userCredentialDAOResponse = userAuthRepository.getUserByLogin(userCredentials.login())
////                .orElseThrow(() -> new AppException("Unknown user", HttpStatus.IM_USED));
////
////        if (passwordEncoder.matches(CharBuffer.wrap((userCredentials.password())), userCredentialDAOResponse.password())) {
////            return ConvertUserCredentialDAOResponseToUserCredentialResponse(userCredentialDAOResponse);
////        }
////        throw new AppException("Unknown user", HttpStatus.IM_USED);
////    }
////
////    private UserCredentialResponse ConvertUserCredentialDAOResponseToUserCredentialResponse(UserCredentialDAOResponse userCredentialDAOResponse) {
////        return new UserCredentialResponse(userCredentialDAOResponse.id(), userCredentialDAOResponse.firstName(), userCredentialDAOResponse.lastName(), userCredentialDAOResponse.login(), null);
////    }
//
//}
