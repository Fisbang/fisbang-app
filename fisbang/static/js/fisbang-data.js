var PlotVar = {};

$(document).ready(function() {
    console.log("document ready2");

    PlotVar.options = {
        series: {
            lines: {
                show: true
            },
            points: {
                show: true
            }
        },
        grid: {
            hoverable: true //IMPORTANT! this is needed for tooltip to work
        },
        yaxis: {
            min: 0,
        },
        xaxes: [{
            mode: 'time'
        }],
        tooltip: true,
        tooltipOpts: {
            content: "'%s' of %x.1 is %y.4",
            shifts: {
                x: -60,
                y: 25
            }
        }
    };

    PlotVar.data = []
    PlotVar.data.push({data: [], label: ""})

    PlotVar.plotObj = $.plot($("#flot-line-chart"), 
                             PlotVar.data,
                             PlotVar.options);

    $('#device-select').change(function(data) {
        console.log("Device changed");
        device_id = this.value
        
        PlotVar.data = []
        PlotVar.plotObj.setData(PlotVar.data);
        PlotVar.plotObj.draw();

        $.ajax({
            url: "api/device/"+device_id,
            username: "ricky.hariady@gmail.com",
            password: "zrxvospwd",
            success:function(result){
                console.log("Got device details : "+JSON.stringify(result));
                PlotVar.device = result;

                sensors = PlotVar.device["sensors"]
                for (i=0;i<sensors.length;i++) {
                    sensor_id = sensors[i]
                    $.ajax({
                        url: "api/sensor/"+sensor_id+"/data",
                        username: "ricky.hariady@gmail.com",
                        password: "zrxvospwd",
                        success:function(result){
                            console.log("Get Sensor Data : "+JSON.stringify(result));
                            data = []
                            for(i=0;i<result.length;i++) {
                                data.push([result[i].time*1000, result[i].value])
                            }
                            PlotVar.data.push({data: data, label: sensor_id});

                            PlotVar.plotObj.setData(PlotVar.data);
                            PlotVar.plotObj.setupGrid(); //only necessary if your new data will change the axes or grid
                            PlotVar.plotObj.draw();
                        }
                    });
                }
            }
        });
    });

    default_device = $('#device-select').first()[0].value
    $('#device-select').val(default_device).trigger('change');

});

