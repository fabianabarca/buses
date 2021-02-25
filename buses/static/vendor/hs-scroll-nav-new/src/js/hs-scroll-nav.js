/*
* HSScrollNav Plugin
* @version: 3.0.0 (Mon, 08 Jun 2020)
* @requires: jQuery v3.0 or later, Bootstrap 4.5 or later
* @author: HtmlStream
* @event-namespace: .HSScrollNav
* @license: Htmlstream Libraries (https://htmlstream.com/)
* Copyright 2020 Htmlstream
*/

export default class HSScrollNav {
	constructor(element, config) {
		this.element = element;
		this.defaults = {
			topLevelComponent: 'html, body',
			target: null,
			duration: 400,
			offset: 0,
			easing: 'linear',
			beforeScroll: null,
			afterScroll: null,
			breakpoint: 769
		};
		this.config = config;
	}
	
	init() {
		const self = this,
			element = self.element,
			dataSettings = $(element).attr('data-hs-scroll-nav-options') ? JSON.parse($(element).attr('data-hs-scroll-nav-options')) : {};
		
		self.config = Object.assign({}, self.defaults, dataSettings, self.config);
		
		self._bindEvents();
		
		$(element).scrollspy(self.config);
	}
	
	_bindEvents() {
		const self = this;
		
		$(self.config.target).on('click', 'a:not([href="#"]):not([href="#0"])', function (e) {
			let hash,
				offsetTop;
			
			e.preventDefault();
			
			if ($.isFunction(self.config.beforeScroll)) {
				self.config.beforeScroll();
			}
			
			if (this.hash !== '' && $(this.hash).length) {
				hash = this.hash;
				//offsetTop = ($(hash).offset().top + 2) - self.config.offset;
				offsetTop = self.config.topLevelComponent == 'html, body' ?
					($(hash).offset().top + 2) - self.config.offset :
					$(self.config.topLevelComponent).scrollTop() - $(self.config.topLevelComponent).offset().top + (($(hash).offset().top + 2) - self.config.offset);
				
				// Smooth scroll
				$(self.config.topLevelComponent).animate({
					scrollTop: offsetTop
				}, {
					duration: self.config.duration,
					easing: self.config.easing,
					complete: function () {
						if (history.replaceState) {
							history.replaceState(null, null, hash);
						}
						
						if ($.isFunction(self.config.afterScroll)) {
							self.config.afterScroll();
						}
					}
				});
				
				return false;
			}
		});
	}
}
