package com.slowcampus.account;

import java.sql.SQLException;

import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.slowcampus.account.AccountService;
import com.slowcampus.config.BasicResponse;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
//import com.google.cloud.bigquery.BigQuery;
//import com.google.cloud.bigquery.BigQueryException;
//import com.google.cloud.bigquery.BigQueryOptions;
//import com.google.cloud.bigquery.QueryJobConfiguration;
//import com.google.cloud.bigquery.TableResult;
@ApiResponses(value = { @ApiResponse(code = 401, message = "Unauthorized", response = BasicResponse.class),
		@ApiResponse(code = 403, message = "Forbidden", response = BasicResponse.class),
		@ApiResponse(code = 404, message = "Not Found", response = BasicResponse.class),
		@ApiResponse(code = 500, message = "Failure", response = BasicResponse.class) })


@RestController
@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RequestMapping(value = "/api")
@Api
public class AccountController {
	@Autowired
	AccountService service;
	@ResponseBody
	@RequestMapping(value = "/user/signup", method = RequestMethod.POST,  produces = "application/json;charset=UTF-8")
	@ApiOperation("로그인")
	private Object signin(@RequestParam String user_id, @RequestParam String user_pw) throws SQLException {
		BasicResponse result = new BasicResponse();
		result.status = true;
		System.out.println(user_id+" "+user_pw);
		Object accountVO = service.getUser(user_id, user_pw);
		System.out.println(accountVO);
		if(accountVO == null) {
			result.status = false;
			result.data = "존재하지 않는 계정입니다.";
			return result;
		}else {
			return accountVO;
		}
	}

}



