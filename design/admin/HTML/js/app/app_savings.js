$(function	()	{

	//Morris Chart

	var barChart = Morris.Bar({
	  element: 'barChart',
	  data: [
		{ y: 'Jan', a: 100, b: 90 },
		{ y: 'Feb', a: 75,  b: 65 },
		{ y: 'Mar', a: 50,  b: 40 },
		{ y: 'Apr', a: 75,  b: 65 },
		{ y: 'Mei', a: 50,  b: 40 },
		{ y: 'Jun', a: 75,  b: 65 },
		{ y: 'Jul', a: 100, b: 90 }
	  ],
	  xkey: 'y',
	  ykeys: ['a', 'b'],
	  grid: false,
	  labels: ['Actual', 'Prediction'],
	  barColors: ['#5EE1B1', '#3BC894'],
	  gridTextColor : '#fff'
	});

	var lineChart = Morris.Line({
		element: 'lineChart',
		data: [
			{ y: '2015', a: 30,  b: 30 },
			{ y: '2016', a: 40,  b: 35 },
			{ y: '2017', a: 50,  b: 40 },
			{ y: '2018', a: 60,  b: 45 },
			{ y: '2019', a: 70,  b: 50 },
			{ y: '2020', a: 80,  b: 55 },
			{ y: '2021', a: 90, b: 60 }
		],
		xkey: 'y',
		grid: false,
		ykeys: ['a', 'b'],
		labels: ['Actual', 'Prediction'],
		lineColors: ['#8CB4BC', '#538792'],
		gridTextColor : '#fff'
	});


	//Sparkline
	$('#visits').sparkline([15,19,20,22,33,27,31,27,19,30,21,10,15,18,25,9], {
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
			donutChart.redraw();
			lineChart.redraw();
			barChart.redraw();			
			
			$.plot($('#placeholder'), [init], options);
		},500);	
	});
	
	$('.size-toggle').click(function()	{
		//resize morris chart
		setTimeout(function() {
			donutChart.redraw();
			lineChart.redraw();
			barChart.redraw();	

			$.plot($('#placeholder'), [init], options);			
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
		$('#visits').sparkline([15,19,20,22,33,27,31,27,19,30,21,10,15,18,25,9], {
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
			
			$.plot($('#placeholder'), [init], options);
		},500);
	});
	
	$(window).load(function(e)	{
	
		//Number Animation
		var currentUser = $('#userCount').text();
		$({numberValue: 0}).animate({numberValue: currentUser}, {
			duration: 2500,
			easing: 'linear',
			step: function() { 
				$('#userCount').text(Math.ceil(this.numberValue)); 
			}
		});
				
		var currentServerload = $('#serverloadCount').text();
		$({numberValue: 0}).animate({numberValue: currentServerload}, {
			duration: 2500,
			easing: 'linear',
			step: function() { 
				$('#serverloadCount').text(Math.ceil(this.numberValue)); 
			}
		});
			
		var currentOrder = $('#orderCount').text();
		$({numberValue: 0}).animate({numberValue: currentOrder}, {
			duration: 2500,
			easing: 'linear',
			step: function() { 
				$('#orderCount').text(Math.ceil(this.numberValue)); 
			}
		});
			
		var currentVisitor = $('#visitorCount').text();
		$({numberValue: 0}).animate({numberValue: currentVisitor}, {
			duration: 2500,
			easing: 'linear',
			step: function() { 
				$('#visitorCount').text(Math.ceil(this.numberValue)); 
			}
		});
	
		setInterval(function() {
			var currentNumber = $('#userCount').text();
			var randomNumber = Math.floor(Math.random()*20) + 1;
			var newNumber = parseInt(currentNumber, 10) + parseInt(randomNumber, 10); 
		
			$({numberValue: currentNumber}).animate({numberValue: newNumber}, {
				duration: 500,
				easing: 'linear',
				step: function() { 
					$('#userCount').text(Math.ceil(this.numberValue)); 
				}
			});
		}, 3000);
			
		setInterval(function() {
			var currentNumber = $('#visitorCount').text();
			var randomNumber = Math.floor(Math.random()*50) + 1;
			var newNumber = parseInt(currentNumber, 10) + parseInt(randomNumber, 10); 
		
			$({numberValue: currentNumber}).animate({numberValue: newNumber}, {
				duration: 500,
				easing: 'linear',
				step: function() { 
					$('#visitorCount').text(Math.ceil(this.numberValue)); 
				}
			});
		}, 5000);
	});
});
