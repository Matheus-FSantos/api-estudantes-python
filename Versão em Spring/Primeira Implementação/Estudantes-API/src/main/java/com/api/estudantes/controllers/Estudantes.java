package com.api.estudantes.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.api.estudantes.domain.model.Estudante;
import com.api.estudantes.domain.repository.EstudanteRepository;

@RestController
@RequestMapping("/estudantes")
public class Estudantes {
	
	@Autowired
	private EstudanteRepository estudanteRepository;
	
	@GetMapping
	public ResponseEntity<List<Estudante>> get() {
		List<Estudante> estudantes = estudanteRepository.findAll();
		
		if(estudantes != null)
			return ResponseEntity.ok().body(estudantes);
		
		return ResponseEntity.notFound().build();
	}
	
	
	@GetMapping("/{id}")
	public ResponseEntity<Estudante> getById(@PathVariable Long id){
		return estudanteRepository.findById(id).map(estudante -> ResponseEntity.ok().body(estudante)).orElse(ResponseEntity.notFound().build());
	}
	
	@PostMapping
	@ResponseStatus(HttpStatus.CREATED)
	public Estudante post(@RequestBody Estudante estudante){
		return estudanteRepository.save(estudante);
	}
	
	@DeleteMapping("/{id}")
	public ResponseEntity<Void> delete(@PathVariable Long id){
		if(!estudanteRepository.existsById(id))
			return ResponseEntity.notFound().build();
		
		estudanteRepository.deleteById(id);
		return ResponseEntity.noContent().build();
	}
}