package com.slowcampus.dongwon;
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


import com.slowcampus.config.BasicResponse;
import com.slowcampus.dongwon.*;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;

@ApiResponses(value = { @ApiResponse(code = 401, message = "Unauthorized", response = BasicResponse.class),
		@ApiResponse(code = 403, message = "Forbidden", response = BasicResponse.class),
		@ApiResponse(code = 404, message = "Not Found", response = BasicResponse.class),
		@ApiResponse(code = 500, message = "Failure", response = BasicResponse.class) })


@RestController
@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RequestMapping(value = "/api")
@Api
public class dongwonController {
	@Autowired
	dongwonService service;
	
	@ResponseBody
	@RequestMapping(value = "/dongwon/dbtest", method = RequestMethod.GET,  produces = "application/json;charset=UTF-8")
	@ApiOperation("dongwon-cloudsql-test-v-1")
	private Object dongwonTest() throws SQLException {
		BasicResponse result = new BasicResponse();
		result.status = true;
		Object DongwonVO = service.getInfo();
		System.out.println(DongwonVO);
		return DongwonVO;
	}

}
