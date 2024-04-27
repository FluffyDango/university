//package com.straysafe.backend.repository.mapper;
//
//import com.straysafe.backend.domain.UserCredentialDAOResponse;
//import org.springframework.jdbc.core.RowMapper;
//
//import java.sql.ResultSet;
//import java.sql.SQLException;
//
//public class UserCredentialsMapper implements RowMapper<UserCredentialDAOResponse> {
//    @Override
//    public UserCredentialDAOResponse mapRow(ResultSet resultSet, int rowNum) throws SQLException {
//
//        return new UserCredentialDAOResponse(
//                resultSet.getLong("pid"),
//                resultSet.getString("first_name"),
//                resultSet.getString("last_name"),
//                resultSet.getString("login"),
//                resultSet.getString("password")
//        );
//    }
//}
