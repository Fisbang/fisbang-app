$(function () {
    
    //Flot Chart
    //Website traffic chart				
    // var init = { data: [[0, 50], [1, 80], [2, 50], [3, 80], [4, 70], [5,90], [6, 80], [7, 80], [8, 10], [9, 12], [10, 10]],
    //     	 label: "Visitor2"
    //            };
    var init = { data: [],
        	 label: ""
               };
    var current_date = (new Date()).getTime();
    var offset_date = 1000 * 60 * 60 * 24;
    var yesterday_date = current_date - offset_date;
    // var yesterday_date = current_date;
    // yesterday_date.setDate(yesterday_date.getDate() - 1);

    console.log("current date : "+current_date);
    console.log("yesterday date : "+yesterday_date);

    //var init;
    var options = {	
	series: {
	    lines: {
		show: true, 
		fill: true,
		fillColor: 'rgba(121,206,167,0.2)'
	    },
	    points: {
		show: false,
		radius: '4.5'
	    }
	},
	grid: {
	    hoverable: true,
	    clickable: true
	},
        xaxis: {
            mode: "time",
            timeformat: "%H:%M",
            minTickSize: [1, "hour"],
            timezone: "browser",
            min: yesterday_date,
            max: current_date
        },
	colors: ["#37b494"]
    };
    var mainPlot;
    
    mainPlot = $.plot($('#placeholder'), [init], options);
    
    $("<div id='tooltip'></div>").css({
	position: "absolute",
	display: "none",
	border: "1px solid #222",
	padding: "4px",
	color: "#fff",
	"border-radius": "4px",
	"background-color": "rgb(0,0,0)",
	opacity: 0.90
    }).appendTo("body");

    $("#placeholder").bind("plothover", function (event, pos, item) {

	var str = "(" + pos.x.toFixed(2) + ", " + pos.y.toFixed(2) + ")";
	$("#hoverdata").text(str);
	
	if (item) {
	    var x = item.datapoint[0],
	    y = item.datapoint[1];
	    
	    $("#tooltip").html(y)
		.css({top: item.pageY+5, left: item.pageX+5})
		.fadeIn(200);
	} else {
	    $("#tooltip").hide();
	}
    });

    $("#placeholder").bind("plotclick", function (event, pos, item) {
	if (item) {
	    $("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
	    mainPlot.highlight(item.series, item.datapoint);
	}
    });
    
    // var animate = function () {
    //     $('#placeholder').animate( {tabIndex: 0}, {
    // 	    duration: 3000,
    // 	    step: function ( now, fx ) {

    // 		var r = $.map( init.data, function ( o ) {
    // 		    return [[ o[0], o[1] * fx.pos ]];
    // 		});

    // 		plot.setData( [{ data: r }] );
    // 		plot.draw();
    // 	    }	
    // 	});
    // }
    
    // animate();


    //Flot Chart
    //Website traffic chart				
    // var init2 = { data: [[0, 5], [1, 8], [2, 5], [3, 8], [4, 7], [5,9], [6, 8], [7, 8], [8, 10], [9, 12], [10, 10]],
    //     	  label: "Visitor3"
    //     	},
    options = {	
	series: {
	    lines: {
		show: true, 
		fill: true,
		fillColor: 'rgba(121,206,167,0.2)'
	    },
	    points: {
		show: false,
		radius: '4.5'
	    }
	},
	grid: {
	    hoverable: true,
	    clickable: true
	},
        xaxis: {
            mode: "time",
            timeformat: "%H:%M",
            minTickSize: [1, "hour"],
            timezone: "browser",
            min: yesterday_date,
            max: current_date
        },
	colors: ["#37b494"]
    };
    var devicePlot;
    
    devicePlot = $.plot($('#placeholder2'), [], options);
    
    $("<div id='tooltip'></div>").css({
	position: "absolute",
	display: "none",
	border: "1px solid #222",
	padding: "4px",
	color: "#fff",
	"border-radius": "4px",
	"background-color": "rgb(0,0,0)",
	opacity: 0.90
    }).appendTo("body");

    $("#placeholder2").bind("plothover", function (event, pos, item) {

	var str = "(" + pos.x.toFixed(2) + ", " + pos.y.toFixed(2) + ")";
	$("#hoverdata").text(str);
	
	if (item) {
	    var x = item.datapoint[0],
	    y = item.datapoint[1];
	    
	    $("#tooltip").html(y)
		.css({top: item.pageY+5, left: item.pageX+5})
		.fadeIn(200);
	} else {
	    $("#tooltip").hide();
	}
    });

    $("#placeholder2").bind("plotclick", function (event, pos, item) {
	if (item) {
	    $("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
	    devicePlot.highlight(item.series, item.datapoint);
	}
    });
    

    //var animate2 = function () {
    //   $('#placeholder2').animate2( {tabIndex: 0}, {
    //	   duration: 3000,
    //	   step: function ( now, fx2 ) {

    //			 var r2 = $.map( init2.data, function ( o ) {
    //				  return [[ o[0], o[1] * fx2.pos ]];
    //			});

    //			 devicePlot.setData( [{ data: r2 }] );
    //		 devicePlot.draw();
    //		}	
    //	});
    //}
    
    //animate2();


    //Sparkline
    $('#energy').sparkline([], {
	type: 'bar', 
	barColor: '#FC8675',	
	height:'35px',
	weight:'96px'
    });
    $('#balances').sparkline([], {
	type: 'bar', 
	barColor: '#65CEA7',	
	height:'35px',
	weight:'96px'
    });
    
    //Timeline color box
    $('.timeline-img').colorbox({
	rel:'group1',
	width:"90%",
	maxWidth:'800px'
    });

    //Resize graph when toggle side menu
    $('.navbar-toggle').click(function()	{
	setTimeout(function() {
	    // donutChart.redraw();
	    lineChart.redraw();
	    barChart.redraw();			
	    
	    $.plot($('#placeholder'), [], options);
	},500);	
    });
    
    $('.size-toggle').click(function()	{
	//resize morris chart
	setTimeout(function() {
	    donutChart.redraw();
	    lineChart.redraw();
	    barChart.redraw();	

	    $.plot($('#placeholder'), [], options);			
	},500);
    });

    //Refresh statistic widget
    $('.refresh-button').click(function() {
	var _overlayDiv = $(this).parent().children('.loading-overlay');
	_overlayDiv.addClass('active');
	
	setTimeout(function() {
	    _overlayDiv.removeClass('active');
	}, 2000);
	
	return false;
    });
    
    $(window).resize(function(e)	{
	
	//Sparkline
	$('#energy').sparkline([], {
	    type: 'bar', 
	    barColor: '#fa4c38',	
	    height:'35px',
	    weight:'96px'
	});
	$('#balances').sparkline([], {
	    type: 'bar', 
	    barColor: '#92cf5c',	
	    height:'35px',
	    weight:'96px'
	});

	//resize morris chart
	setTimeout(function() {
	    donutChart.redraw();
	    lineChart.redraw();
	    barChart.redraw();			
	    
	    $.plot($('#placeholder'), [], options);
	    $.plot($('#placeholder2'), [], options);
	},500);
    });
    
    $(window).load(function(e)	{

	var environments = [];
        var sensors = [];
	var sensorData = {};
        var mainPlotData = [];
        var devicePlotData = [];

	var updateMainEnvironments = function() {
	    console.log("Retrieving main environment");
	    $.ajax({
		url: "/api/environment?collapse=true",
		success:function(result){
		    console.log("Got environments : "+JSON.stringify(result));
		    environments = result;

                    for(i=0;i<environments.length;i++){
                        updateMainPowerSensor(environments[i]);
                    }
		}
	    });
	};

        var updateMainPowerSensor = function(environment) {
	    console.log("Retrieving main power sensor");
	    $.ajax({
		url: "/api/sensor?environment_id="+environment["id"],
		success:function(result){
		    console.log("Got sensors : "+JSON.stringify(result));
                    environment["sensors"] = result;
                    for(i=0;i<environment["sensors"].length;i++){
                        if(environment["sensors"][i]["type"] == "MAIN POWER"){
                            updateMainPowerSensorData(environment["sensors"][i], environment["name"])
                        }
                    }
		}
	    });
        }

        var updateMainPowerSensorData = function(sensor, environment_name) {
	    $.ajax({
		url: "/api/sensor/"+sensor["token"]+"/data?resample=T",
		success:function(result){
		    console.log("Got sensors data (hourly): "+JSON.stringify(result));

                    var main_data = []
                    for(i=0;i<result.length;i++){
                        main_data.push([result[i]["timestamp"]*1000,result[i]["value"]]);
                    }
                    mainPlotData.push({data: main_data, label: environment_name})
                    updatePlotData(mainPlot, mainPlotData)
		},
                error: function (xhr, ajaxOptions, thrownError) {
                    alert(xhr.status);
                    alert(thrownError);
                }
	    });

	    $.ajax({
		url: "/api/sensor/"+sensor["token"]+"/data?resample=D",
		success:function(result){
		    console.log("Got sensors data (daily): "+JSON.stringify(result));

                    var current_date = new Date();

                    $('#hours-count-daily').text(current_date.getHours());

                    current_date.setHours(0,0,0,0);

                    var last_daily_energy = 0;
                    for(i=0;i<result.length;i++){
                        console.log(result[i]["timestamp"]*1000);
                        console.log(current_date.getTime())
                        if(result[i]["timestamp"]*1000 >= current_date.getTime()){
                            last_daily_energy = result[i]["value"]/1000;
                        }
                    }

                    $('#energy-count-daily').text(last_daily_energy.toFixed(3));

	            $({numberValue: 0}).animate({numberValue: last_daily_energy.toFixed(3)}, {
	                duration: 1000,
	                easing: 'linear',
	                step: function() { 
		            $('#today-energy').text(Math.ceil(this.numberValue)+" kWh"); 
	                }
	            });

	            $({numberValue: 0}).animate({numberValue: last_daily_energy*900}, {
	                duration: 1000,
	                easing: 'linear',
	                step: function() { 
		            $('#current-balance').text("Rp " + Math.ceil(this.numberValue)); 
	                }
	            });

                    var monthly_energy = [];
                    for(i=0;i<result.length;i++)
                        monthly_energy.push(result[i]["value"]/1000);
                                    
                    $('#energy').sparkline(monthly_energy, {
	                type: 'bar', 
	                barColor: '#FC8675',	
	                height:'35px',
	                weight:'96px'
                    });

                    var monthly_balance = [];
                    for(i=0;i<result.length;i++)
                        monthly_balance.push((result[i]["value"]/1000) * 900);

                    $('#balances').sparkline(monthly_balance, {
	                type: 'bar',
	                barColor: '#FC8675',
	                height:'35px',
	                weight:'96px'
                    });

		}
	    });

	    $.ajax({
		url: "/api/sensor/"+sensor["token"]+"/data?resample=M",
		success:function(result){
		    console.log("Got sensors data (monthly): "+JSON.stringify(result));

                    var current_date = new Date();

                    $('#days-count-monthly').text(current_date.getDate());

                    current_date.setDate(1);
                    current_date.setHours(0,0,0,0);

                    var last_monthly_energy = 0;
                    for(i=0;i<result.length;i++){
                        console.log(result[i]["timestamp"]*1000);
                        console.log(current_date.getTime())
                        if(result[i]["timestamp"]*1000 > current_date.getTime()){
                            last_monthly_energy = result[i]["value"]/1000;
                        }
                    }

                    var last_monthly_balance = last_monthly_energy;
                    console.log(last_monthly_balance);

                    $('#energy-count-monthly').text(last_monthly_energy.toFixed(3))

                    $('#currentEnergy').text(Math.ceil(last_monthly_energy)); 
                    $('#currentBalance').text(Math.ceil(last_monthly_energy));

		}
	    });
        }

        var updatePlotData = function(plt, data) {
	    console.log("Update plot : "+JSON.stringify(data));
	    console.log(plt);

            var max = 100
            for(i=0;i<data.length;i++){
                for(j=0;j<data[i]["data"].length;j++){
                    max = Math.max(max, data[i]["data"][j][1])
                }
            }

            plt.setData( data );
            plt.getOptions().yaxes[0].max = max + 100;
            plt.setupGrid()
            plt.draw();

        }

	var updateDevices = function() {
	    $.ajax({
		url: "/api/device",
		success:function(result){
		    console.log("Got devices : "+JSON.stringify(result));
		    devices = result;
                    for(i=0;i<devices.length;i++){
                        updateDevicePowerSensor(devices[i]);
                    }

		}
	    });
	};

        var updateDevicePowerSensor = function(device) {
	    console.log("Retrieving device power sensor");
	    $.ajax({
		url: "/api/sensor?device_id="+device["id"],
		success:function(result){
		    console.log("Got sensors : "+JSON.stringify(result));
                    device["sensors"] = result;
                    for(i=0;i<device["sensors"].length;i++){
                        if(device["sensors"][i]["type"] == "POWER"){
                            name = device["device_type"] + " - " + device["merk"] + " - " + device["type"] + " - " + device["wattage"] + "W"
                            updateDevicePowerSensorData(device["sensors"][i], name)
                        }
                    }
		}
	    });
        }

        var updateDevicePowerSensorData = function(sensor, device_name) {
	    console.log("Retrieving device power sensor data");
	    $.ajax({
		url: "/api/sensor/"+sensor["token"]+"/data?resample=T",
		success:function(result){
		    console.log("Got sensors data (hourly): "+JSON.stringify(result));

                    var device_data = []
                    for(i=0;i<result.length;i++){
                        device_data.push([result[i]["timestamp"]*1000,result[i]["value"]]);
                    }
                    devicePlotData.push({data: device_data, label: device_name})
                    updatePlotData(devicePlot, devicePlotData)
		},
                error: function (xhr, ajaxOptions, thrownError) {
                    alert(xhr.status);
                    alert(thrownError);
                }
	    });

        }

	updateMainEnvironments();
	updateDevices();


	//Number Animation
	// var today_energy = $('#today-energy').text();
	// $({numberValue: 0}).animate({numberValue: today_energy}, {
	//     duration: 2500,
	//     easing: 'linear',
	//     step: function() { 
	// 	$('#today-energy').text(Math.ceil(this.numberValue)); 
	//     }
	// });
	
	// var ratio_from_power_capacity = $('#ratio-from-power-capacity').text();
	// $({numberValue: 0}).animate({numberValue: ratio_from_power_capacity}, {
	//     duration: 2500,
	//     easing: 'linear',
	//     step: function() { 
	// 	$('#ratio_from_power_capacity').text(Math.ceil(this.numberValue)); 
	//     }
	// });
	
	// var current_balance = $('#current-balance').text();
	// $({numberValue: 0}).animate({numberValue: current_balance}, {
	//     duration: 2500,
	//     easing: 'linear',
	//     step: function() { 
	// 	$('#current_balance').text(Math.ceil(this.numberValue)); 
	//     }
	// });
	
	// var ratio_from_max_budget = $('#ratio-from-max-budget').text();
	// $({numberValue: 0}).animate({numberValue: ratio_from_max_budget}, {
	//     duration: 2500,
	//     easing: 'linear',
	//     step: function() { 
	// 	$('#ratio-from-max-budget').text(Math.ceil(this.numberValue)); 
	//     }
	// });
	
    });
});
