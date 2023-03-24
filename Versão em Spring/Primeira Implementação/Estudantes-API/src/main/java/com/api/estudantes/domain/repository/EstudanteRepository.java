package com.api.estudantes.domain.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.api.estudantes.domain.model.Estudante;

public interface EstudanteRepository extends JpaRepository<Estudante, Long>{

}