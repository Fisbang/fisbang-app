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
		show: true,
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
            min: yesterday_date,
            max: current_date
        },
	colors: ["#37b494"]
    };
    var plot;
    
    plot = $.plot($('#placeholder'), [init], options);
    
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
	    
	    $("#tooltip").html("Visitor : " + y)
		.css({top: item.pageY+5, left: item.pageX+5})
		.fadeIn(200);
	} else {
	    $("#tooltip").hide();
	}
    });

    $("#placeholder").bind("plotclick", function (event, pos, item) {
	if (item) {
	    $("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
	    plot.highlight(item.series, item.datapoint);
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
		show: true,
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
            min: yesterday_date,
            max: current_date
        },
	colors: ["#37b494"]
    },
    plot;
    
    plot2 = $.plot($('#placeholder2'), [], options);
    
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
	    
	    $("#tooltip").html("Visitor : " + y)
		.css({top: item.pageY+5, left: item.pageX+5})
		.fadeIn(200);
	} else {
	    $("#tooltip").hide();
	}
    });

    $("#placeholder2").bind("plotclick", function (event, pos, item) {
	if (item) {
	    $("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
	    plot2.highlight(item.series, item.datapoint);
	}
    });
    

    //var animate2 = function () {
    //   $('#placeholder2').animate2( {tabIndex: 0}, {
    //	   duration: 3000,
    //	   step: function ( now, fx2 ) {

    //			 var r2 = $.map( init2.data, function ( o ) {
    //				  return [[ o[0], o[1] * fx2.pos ]];
    //			});

    //			 plot2.setData( [{ data: r2 }] );
    //		 plot2.draw();
    //		}	
    //	});
    //}
    
    //animate2();


    //Sparkline
    $('#energy').sparkline([15,19,20,22,33,27,31,27,19,30,21,10,15,18,25,9], {
	type: 'bar', 
	barColor: '#FC8675',	
	height:'35px',
	weight:'96px'
    });
    $('#balances').sparkline([220,160,189,156,201,220,104,242,221,111,164,242,183,165], {
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
	$('#energy').sparkline([15,19,20,22,33,27,31,27,19,30,21,10,15,18,25,9], {
	    type: 'bar', 
	    barColor: '#fa4c38',	
	    height:'35px',
	    weight:'96px'
	});
	$('#balances').sparkline([220,160,189,156,201,220,104,242,221,111,164,242,183,165], {
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
        var house_environment_id;
        var house_environment_name;
	var devices = [];
        var sensors = [];
	var sensorData = {};
        var mainPlotData = [];
        var devicePlotData = [];

	var updateEnvironments = function() {
	    $.ajax({
		url: "/api/environment",
		success:function(result){
		    console.log("Got environments : "+JSON.stringify(result));
		    environments = result;

	            console.log("Retrieving house environment id");
                    for(i=0;i<environments.length;i++){
                        if(environments[i]["environment_type"] == "HOUSE") {
                            house_environment_id = environments[i]["id"];
                            house_environment_name = environments[i]["name"];
                            break;
                        }
                    }
	            console.log("Finish retrieving house environment id. Result = "+house_environment_id);

	            updateDevices();
		}
	    });
	};

	var updateDevices = function() {
	    $.ajax({
		url: "/api/device",
		success:function(result){
		    console.log("Got devices : "+JSON.stringify(result));
		    devices = result;
                    updateSensors();
		}
	    });
	};


	var updateSensors = function() {
	    $.ajax({
		url: "/api/sensor",
		success:function(result){
		    console.log("Got sensors : "+JSON.stringify(result));
		    sensors = result;

	            console.log("Retrieving house current sensor id");
                    for(i=0;i<sensors.length;i++){
                        if(sensors[i]["environment_id"] == house_environment_id && sensors[i]["device_id"] == null) {
                            if(sensors[i]["type"]=="CURRENT"){
                                house_sensor_id = sensors[i]["id"];
                                break;
                            }
                        }
                    }
	            console.log("Finish retrieving house sensor id. Result = "+house_sensor_id);

                    updateSensorsData();
		}
	    });
	};

	var updateSensorsData = function() {
	    console.log("Retrieving sensor data");
	    for(i=0;i<sensors.length;i++){
		$.ajax({
		    url: "/api/sensor/"+sensors[i]["id"]+"/data?resample=H",
                    indexValue: i,
                    // async: false,
		    success:function(result){
			console.log("Got sensors data : "+JSON.stringify(result));
                        sensor_id = sensors[this.indexValue]["id"]
			sensorData[sensor_id] = result;
                        if(sensor_id == house_sensor_id) {
                            var main_data = []
                            var max = 100
                            for(i=0;i<result.length;i++){
                                max = Math.max(max, result[i]["value"]*220)
                                main_data.push([result[i]["timestamp"]*1000,result[i]["value"]*220]);
                            }
                            mainPlotData.push({data: main_data, label: house_environment_name})
			    console.log("mainPlotData : "+JSON.stringify(mainPlotData));
			    console.log(plot);
                            plot.setData( mainPlotData );
                            plot.getOptions().yaxes[0].max = max + 100;
                            plot.setupGrid()
                            plot.draw();
                            // console.log("plot data : "+JSON.stringify(plot.getData()));


		            $.ajax({
		                url: "/api/sensor/"+sensors[this.indexValue]["id"]+"/data?resample=D",
                                indexValue: this.indexValue,
                                // async: false,
		                success:function(result){
                                    var current_date = new Date();
                                    $('#hours-count-daily').text(current_date.getHours());

                                    var last_daily_energy = 0;
                                    var last_daily_timestamp = 0;
                                    for(i=0;i<result.length;i++){
                                        if(result[i]["timestamp"] > last_daily_timestamp){
                                            last_daily_energy = result[i]["value"]*220/1000;
                                            last_daily_timestamp = result[i]["timestamp"];
                                        }
                                    }

                                    $('#energy-count-daily').text(last_daily_energy.toFixed(3));

	                            $({numberValue: 0}).animate({numberValue: last_daily_energy.toFixed(3)}, {
	                                duration: 3000,
	                                easing: 'linear',
	                                step: function() { 
		                            $('#today-energy').text(Math.ceil(this.numberValue)); 
	                                }
	                            });

	                            $({numberValue: 0}).animate({numberValue: last_daily_energy*900}, {
	                                duration: 3000,
	                                easing: 'linear',
	                                step: function() { 
		                            $('#current-balance').text(Math.ceil(this.numberValue)); 
	                                }
	                            });

                                    var monthly_energy = [];
                                    for(i=0;i<result.length;i++)
                                        monthly_energy.push(result[i]["value"]*220/1000);
                                    
                                    $('#energy').sparkline(monthly_energy, {
	                                type: 'bar', 
	                                barColor: '#FC8675',	
	                                height:'35px',
	                                weight:'96px'
                                    });


                                }
                            });

		            $.ajax({
		                url: "/api/sensor/"+sensors[this.indexValue]["id"]+"/data?resample=M",
                                indexValue: i,
                                // async: false,
		                success:function(result){
                                    var current_date = new Date();
                                    console.log(current_date.getHours());
                                    $('#days-count-monthly').text(current_date.getDate());

                                    var last_monthly_energy = 0;
                                    var last_monthly_timestamp = 0;
                                    for(i=0;i<result.length;i++){
                                        if(result[i]["timestamp"] > last_monthly_timestamp){
                                            last_monthly_energy = result[i]["value"]*220/1000;
                                            last_monthly_timestamp = result[i]["timestamp"];
                                        }
                                    }
                                    console.log(result);
                                    console.log(last_monthly_energy);

                                    $('#energy-count-monthly').text(last_monthly_energy.toFixed(3))

		                    $('#currentEnergy').text(Math.ceil(last_monthly_energy)); 
		                    $('#currentBalance').text(Math.ceil(last_monthly_energy*900)); 

                                }
                            });

                            return;
                        }

                        for(i=0;i<devices.length;i++){
                            device = devices[i];
                            if(device["sensors"].indexOf(sensor_id) > -1){
                                if(sensors[i]["type"]=="CURRENT"){
                                    var device_data = []
                                    for(j=0;j<result.length;j++){
                                        device_data.push([result[j]["timestamp"]*1000,result[j]["value"]*220]);
                                    }
                                    devicePlotData.push({data: device_data, label: device["device_type"]})
			            console.log("devicePlotData : "+JSON.stringify(devicePlotData));
                                    plot2.setData( devicePlotData );
                                    plot2.setupGrid()
                                    plot2.draw();
                                    // console.log("plot data : "+JSON.stringify(plot2.getData()));
                                    return;
                                }
                            }
                        }
		    },
		});
	    }
	    console.log("Finish retrieving sensor data");
	}

	updateEnvironments();

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
