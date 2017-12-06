$(function(){
	var categorias = {
                exportEnabled: true,
                animationEnabled: true,
                title: {
                    text: "Resultados por Categorías "
                },
                data: [
                {
                    type: "pie", //change it to line, area, bar, pie, etc
                    startAngle: 240,
                    yValueFormatString: "##0",
                    indexLabel: "{label} {y}",
                    dataPoints: [
                        { y: $('#sobresaliente').val(), label: "Platinum" },
                        { y: $('#muybueno').val(), label: "Oro" },
                        { y: $('#bueno').val(), label: "Plata" },
                        { y: $('#bronce').val(), label: "bronce" }
                    ]
                }
                ]
            };
            $("#chartCategories").CanvasJSChart(categorias);
});