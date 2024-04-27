package com.straysafe.backend.domain;

public record UserCredentialDAOResponse(
        Long id,
        String firstName,
        String lastName,
        String login,
        String password
){}
