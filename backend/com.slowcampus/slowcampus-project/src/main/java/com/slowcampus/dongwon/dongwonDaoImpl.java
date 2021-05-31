package com.slowcampus.dongwon;
import java.sql.SQLException;

import java.util.*;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
@Repository
public class dongwonDaoImpl implements dongwonDao{
	@Autowired
	private SqlSession sqlSession;

	@Override
	public ArrayList<dongwonVO> getInfo() throws SQLException {
		// TODO Auto-generated method stub
		dongwonMapper mapper = sqlSession.getMapper(dongwonMapper.class);
		System.out.println(mapper.getInfo());
		return mapper.getInfo();
	}
	
	
}
