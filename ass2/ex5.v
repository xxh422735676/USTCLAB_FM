Theorem example5: forall P Q: Prop,
  (P\/Q)->(Q\/P).
Proof.
intros.
inversion H.
right.
apply H0.
left.
apply H0.
Qed.