;(function($){
	Cross = function($element)
	{
        this.$element = $element;
        this.$container = $element.parent();
        this.id = $element.attr('id');
        this.width = $element.width();
        this.height = $element.height();
        
        this.$formFieldX = $('#id_value_x');
        this.$formFieldY = $('#id_value_y');

        this.minX;
        this.maxX;
        this.minY;
        this.maxY;

        this.handleSize = this.width/100 * 5;
        this.xVal;
        this.yVal;

        this.stage; 
        this.layer;
        this.handle;

        this.init();
	};

    Cross.prototype.init = function(pxPerStep, targetLeft)
    {
        var self = this;
        
        self.initStage();

        self.initAxis();

        self.initHandle();

        self.stage.add(self.layer);
        
        self.setValuesFromFormField();
    };      
	

    Cross.prototype.initStage = function()
    {
        var self = this;

        // create a kineticJS stage that will hold all layers (pov, geosounds, connections, playhead)
        self.stage = new Kinetic.Stage({container: self.id, width: self.width, height: self.height });

        self.stage.getContent().addEventListener('click', function(e)
        {
            var offset = self.$element.offset();
            var x = e.clientX - offset.left - (self.handleSize / 2);
            var y = e.clientY - offset.top - (self.handleSize /2);
            
            console.log(offset);
            console.log(e);
            console.log(x);
            console.log(y);

            x = (x < self.handleSize) ? 0 : x;
            x = (x > self.width - self.handleSize) ? self.width - self.handleSize : x;
            y = (y < self.handleSize) ? 0 : y;
            y = (y > self.height - self.handleSize) ? self.height - self.handleSize : y;

            self.xVal = x / (self.width - self.handleSize);
            self.yVal = y / (self.height - self.handleSize);

            self.layer.clear();
            self.handle.setX(x);
            self.handle.setY(y);
            self.layer.draw();

            self.updateFormFields();
        });   

        self.layer = new Kinetic.Layer();        
    };


    Cross.prototype.initAxis = function()
    {
        var self = this;

        var xAxis = new Kinetic.Line({
            points: [
                {x:0, y:self.height/2},
                {x:self.width, y:self.height/2}
            ],
            stroke: 'black',
        });

        var yAxis = new Kinetic.Line({
            points: [
                {x:self.width/2, y:0},
                {x:self.width/2, y:self.height}
            ],
            stroke: 'black',
        });

        self.layer.add(xAxis);
        self.layer.add(yAxis);        
    };    


    Cross.prototype.initHandle = function()
    {
        var self = this;

        self.minX = self.stage.getX();
        self.maxX = self.stage.getX() + self.stage.getWidth() - self.handleSize;
        self.minY = self.stage.getY();
        self.maxY = self.stage.getY() + self.stage.getHeight() - self.handleSize;        

        self.handle = new Kinetic.Rect({
            width: self.handleSize,
            height: self.handleSize,
            fill: 'black',
            stroke: 'black',
            strokeWidth: 0,
            draggable: true,
            dragBoundFunc: function(pos)
            {
                var x = pos.x;
                var y = pos.y;
                
                x = (x < self.minX) ? self.minX : x;
                x = (x > self.maxX) ? self.maxX : x;
                y = (y < self.minY) ? self.minY : y;
                y = (y > self.maxY) ? self.maxY : y;

                return ({x:x, y:y});
            }
        });   

        self.handle.on("mouseover", function(e) 
        {
            // change cursor 
            self.$element.css({
                'cursor':'pointer',
            });
        });

        self.handle.on("mouseout", function(e) 
        {
            // reset cursor 
            self.$element.css({
                'cursor':'default'
            });
        });

        self.handle.on("dragstart", function(e) 
        {
            //
        });

        self.handle.on("dragend", function(e)
        {
            self.xVal = self.handle.getX() / (self.width - self.handleSize);
            self.yVal = self.handle.getY() / (self.height - self.handleSize);

            self.updateFormFields();
        });                

        self.layer.add(self.handle);    
    };        
	
    Cross.prototype.setValuesFromFormField = function()
    {
        var self = this;

        var value_x = self.$formFieldX.val();
        var value_y = self.$formFieldY.val();

        var x = value_x * (self.width - self.handleSize / 2);
        var y = value_y * (self.height - self.handleSize / 2);

        self.layer.clear();
        self.handle.setX(x);
        self.handle.setY(y);
        self.layer.draw();
    };

	/* calculate the layer's opacity values by the scrollbar progress */
 	Cross.prototype.layerOpacity = function(progress)     
    {
        var self = this;
    	var opacity = (progress * self.maxOpacity > self.minOpacity) ? progress * self.maxOpacity : self.minOpacity;
    	$('.background', self.$container).css({'opacity':opacity});
    };

    Cross.prototype.updateFormFields = function()
    {
        var self = this;

        // round to 3 places after decimal point
        var rounded_value_x = Math.round(self.xVal * 1000) / 1000;
        var rounded_value_y = Math.round(self.yVal * 1000) / 1000;
        
        // update page field
        self.$formFieldX.val(rounded_value_x);

        self.$formFieldY.val(rounded_value_y);
    };
		
})(jQuery);

