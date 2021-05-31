package com.slowcampus.dongwon;
import java.sql.SQLException;
import java.util.*;

public interface dongwonDao {
	public ArrayList<dongwonVO> getInfo() throws SQLException;
}
