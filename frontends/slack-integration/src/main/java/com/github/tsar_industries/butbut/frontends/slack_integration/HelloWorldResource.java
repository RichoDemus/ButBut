package com.github.tsar_industries.butbut.frontends.slack_integration;

import com.github.tsar_industries.butbut.service_layer.api.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;

@Path("/hello")
public class HelloWorldResource
{
	private final Logger logger = LoggerFactory.getLogger(getClass());
	private final Service service;

	@Inject
	public HelloWorldResource(Service service)
	{
		this.service = service;
	}

	@GET
	public String hello()
	{
		logger.info("Someone's saying hello");
		return service.getImage("majsfisk")
				.map(i -> "y hello thar, I founds image")
				.orElseGet(() -> "y hello thar, no image found. If you can read this, continuous deployment works!");
	}
}
