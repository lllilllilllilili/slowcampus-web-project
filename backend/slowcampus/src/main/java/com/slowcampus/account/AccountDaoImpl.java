package com.slowcampus.account;

import java.sql.SQLException;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
@Repository
public class AccountDaoImpl implements AccountDao{
	
	@Autowired
	private SqlSession sqlSession;
	
	@Override
	public AccountVO getUser(String user_id, String user_pw) throws SQLException {
		// TODO Auto-generated method stub
		AccountMapper mapper =sqlSession.getMapper(AccountMapper.class);
		return mapper.getUser(user_id, user_pw);
	}

}
