//package com.straysafe.backend.repository;
//
//import com.straysafe.backend.domain.UserCredentialDAOResponse;
//import com.straysafe.backend.repository.mapper.UserCredentialsMapper;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
//import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
//import org.springframework.jdbc.core.namedparam.SqlParameterSource;
//import org.springframework.stereotype.Repository;
//
//import java.util.Optional;
//
//@Repository
//public class UserAuthRepository implements UserAuthRepositoryInterface{
//
////    private final NamedParameterJdbcTemplate namedParameterJdbcTemplate;
////
////    @Autowired
////    public UserAuthRepository(NamedParameterJdbcTemplate namedParameterJdbcTemplate) {
////        this.namedParameterJdbcTemplate = namedParameterJdbcTemplate;
////    }
////
////    @Override
////    public Optional<UserCredentialDAOResponse> getUserByLogin(String login) {
////        String query = """
////                SELECT pid, first_name, last_name, login, password
////                FROM users
////                WHERE login = :login
////                """;
////        SqlParameterSource params = new MapSqlParameterSource()
////                .addValue("login", login);
////        return namedParameterJdbcTemplate.query(query, params, new UserCredentialsMapper())
////                .stream()
////                .findFirst();
////    }
//}
