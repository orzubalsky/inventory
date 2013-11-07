;(function($){
	Spectrum = function($element, maxOpacity)
	{
	    // init properties
	    this.title = $element.parent().attr('id');
        this.$element = $element;
	    this.$container = $element.parent();
	    this.$formField = this.$container.children('input');

        this.color = $element.parent().css('background-color');	    
        this.minOpacity = 0;
	    this.maxOpacity = maxOpacity;
        this.containerWidth;
        
        // init methods
        this.getDimensions();
        this.interaction();        
	};
	
    /* Calculate the scrollbar container width according to the container and the scrollbar widths */		
    Spectrum.prototype.getDimensions = function() 
    {
        var self = this;
        
		var sliderWidth = self.$element.width();
		var containerWidth = self.$container.width();
		self.containerWidth = containerWidth - sliderWidth;
	};
	
	/* animate the scrollbar on initialization to demo the interaction */
	Spectrum.prototype.animate = function(pxPerStep, targetLeft)
	{
	    var self = this;
	    
        self.interval = setInterval(function() 
        {                
            var left = self.$element.position().left;
            left = (left + pxPerStep < targetLeft) ? left += pxPerStep : targetLeft;
            if (left >= targetLeft) { clearInterval(self.interval); }
            if (self.$container.click(function(e) { clearInterval(self.interval); }));
            self.$element.css({'left':left});
            var progress = left / self.containerWidth;
            self.layerOpacity(progress);

        }, 10); 
        
               
	};	

     /* scrollbar drag interaction animates the slides, clicking on the slides pauses animation */
 	Spectrum.prototype.interaction = function()     
    {
		var self = this;
        var color;
        
        self.$element.bind('mouseenter', function(e) 
        {
            $(this).addClass('hover');
        }); 
        
        self.$element.bind('mouseleave', function(e) 
        {
            $(this).removeClass('hover');
        });
        
        // people can drag the scrollbar 
		self.$element.draggable({
		    axis: "x",
            containment: self.$container,
            start: function(event, ui)
            {
                //
            },
            drag: function(event, ui)
            {
                var progress = (ui.position.left / self.containerWidth);
                self.layerOpacity(progress);
            },
            stop: function(event, ui) 
            {
                var progress = (ui.position.left / self.containerWidth);
                self.updateFormField(progress);
            }
		});
		
		// people can also just click on the scrollbar and reposition it
		self.$container.click(function(e) 
		{
            var xPos;

            if (e.offsetX==undefined) 
            {
                xPos = e.pageX - self.$container.offset().left; 
            }
            else 
            {
                xPos = e.offsetX;
            }            

            var left = xPos - self.$element.width() / 2;

		    if (left < 0) { left = 0; }
		    if (left > self.containerWidth) { left = self.containerWidth; }
		    self.$element.css({'left':left});
		    var progress = xPos / self.containerWidth;
		    self.layerOpacity(progress);
		});
	};
	
	/* calculate the layer's opacity values by the scrollbar progress */
 	Spectrum.prototype.layerOpacity = function(progress)     
    {
        var self = this;
    	var opacity = (progress * self.maxOpacity > self.minOpacity) ? progress * self.maxOpacity : self.minOpacity;
    	$('.color', self.$container).css({'opacity':opacity});
    };

    Spectrum.prototype.updateFormField = function(value)
    {
        var self = this;

        // round to 3 places after decimal point
        var rounded_value = Math.round(value * 1000) / 1000;
        
        // update page field
        self.$formField.val(rounded_value);
    };
		
})(jQuery);